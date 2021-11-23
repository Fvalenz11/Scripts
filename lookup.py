#create a ip lookup file
#usage python3 ip_lookup -i ip.txt -o ip.csv

import sys, os, csv

def ip2int(ip):
    '''
    convert ip to int
    '''
    ip = [int(x) for x in ip.split('.')]
    return ip[0] << 24 | ip[1] << 16 | ip[2] << 8 | ip[3]  # use shift and OR to compose


def int2ip(num):
    '''
    convert int to ip
    '''
    return '%s.%s.%s.%s' % ((num >> 24) & 0xff, (num >> 16) & 0xff, (num >> 8) & 0xff, (num & 0xff))



def read_ip(fname):
    '''
    read ip from file
    '''
    ip_list = []
    with open(fname, 'r') as f:
        for line in f:
            line.strip()
            if line:
                ip_list.append(line.strip())
    return ip_list



def search_ip(ip_list, ip_lookup):
    '''
    search ip
    '''
    result = {}
    for line in ip_lookup:
        if '"' in line:
            continue
        ip_str, cname = line.split(',')
        if ip_str.strip() in ip_list:
            result[ip_str.strip()] = cname.strip()
    return result


def write_csv(result, csv_file):
    '''
    write result to csv file
    '''
    with open(csv_file, 'w') as csvfile:
        fieldnames = ['ip', 'cname']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for ip in result.keys():
            writer.writerow({'ip': ip, 'cname': result[ip]})

def main():
    '''
    main function
    '''
    if len(sys.argv) < 4:
        print('Usage: python ip_lookup.py -i ip.txt -o ip.csv')
        sys.exit(1)
    ip_file = sys.argv[sys.argv.index('-i') + 1]
    ip_lookup_file = sys.argv[sys.argv.index('-o') + 1]
    ip_list = read_ip(ip_file)
    with open(ip_lookup_file, 'r') as f:
        ip_lookup = f.readlines()
    result = search_ip(ip_list, ip_lookup)
    write_csv(result, 'ip_lookup.csv')

if __name__ == '__main__':
    main()
