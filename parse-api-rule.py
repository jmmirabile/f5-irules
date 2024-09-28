#!/usr/bin/env python3

import logging as log
import sys
import argparse


runtime_list = []
pool_dict = {}
uri_dict = {}
empty_list = []
uri_list = []
runtime_count = 0

def append_uridict(uri, value_to_append):
    global uri_dict
    value = uri_dict[uri]
    value.append(value_to_append)
    
    
def append_uri_dict(uri_list, runtime_name):
    for uri in uri_list:
        value = uri_dict[uri]
        value.append(runtime_name)
    
    uri_list.clear()
    
    
def print_func():
    print("def {}()".format(sys._getframe(1).f_code.co_name))


def callersname():
    return sys._getframe(1).f_code.co_name


def checkArgs():
    print_func()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--file", help='file name', required=True)
    #parser.add_argument('-c', "--config", help='config file name', required=False)
    return parser.parse_args()


def app(file):
    '''App logic if not in main - for instance launch a handler'''
    print_func()
    line_num = 0
    global runtime_count
    global uri_list 
    global uri_dict 
    global runtime_list
    global runtime_list 
    global pool_dict
    global empty_list

    with open(file, 'r') as f:
        
        for line in f:
            line_num += 1
            
            if line_num >= 10:
                #print("line num: ", line_num)
                if "uri" in line:
                    curr_list = []
                    uri = line.split()[2]
                    operator = line.split()[1]
                    uri_list.append(uri)
                    if operator:
                        curr_list.append(operator)
                        uri_dict[uri] = curr_list 
        
                    
                elif "pool" in line:
                    runtime_count += 1
                    pool_name = line.split()[1]
                    #print(pool_name)
                    runtime_list.append(pool_name)
                    append_uri_dict(uri_list, pool_name)
                    
                
                elif "wideip" in line:
                    runtime_count += 1
                    wip_name = line.split()[2]
                    #print(wip_name)
                    runtime_list.append(wip_name)
                    append_uri_dict(uri_list, wip_name)
                
    


def main():
    '''Main function'''
    args = checkArgs()
    app(args.file)
    
    for k,v in uri_dict.items():
        #print(k, *v, sep='","', end='"\n')
        print(k, *v, sep=',')
                
    #print(*runtime_list, sep=",")
    
    print("Pool/WIP Count: ", runtime_count)
    

if __name__ == '__main__':
    level = log.DEBUG
    logfmt = '[%(levelname)s] %(asctime)s - %(message)s'
    log.basicConfig(level=level, format=logfmt)
    main()


