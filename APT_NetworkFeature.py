# -*- coding: utf-8 -*-
import json
import os
import pandas as pd
import global_list
from time import time


if __name__ =="__main__":
    start = time()

    APT_network_path = os.path.abspath(".") + "/APT_NetworkFeature/"
    if not os.path.exists(APT_network_path):
        os.makedirs(APT_network_path)

    dataframelist = []

    # ======================获取每个文件的Network Operation信息===========================
    All_APT_json_array = ['BaiXiang-json', 'DarkHotel-json', 'Mirage-json', 'NormanShark-json', 'SinDigoo-json']
    for i in range(len(All_APT_json_array)):
        curDir = All_APT_json_array[i]
        dir_path = os.path.abspath('.') + '/Json/' + curDir + '/'
        files = os.listdir(dir_path)
        num = 1
        for mFile in files:
            with open(dir_path + '/' + mFile, 'r') as fo:
                print "Analysing the %d file" %num
                standard = {}
                standard["Id"] = mFile[:-5]

                tcp_src_ip_list = []
                udp_src_ip_list = []
                tcp_dst_ip_list = []
                udp_dst_ip_list = []
                tcp_src_ports_list = []
                udp_src_ports_list = []
                tcp_dst_ports_list = []
                udp_dst_ports_list = []
                hosts_list = []
                dead_hosts_list = []
                domains_list = []
                dns_list = []
                dns_servers_list = []

                udp_src_ips = 0
                tcp_src_ips = 0
                udp_dst_ips = 0
                tcp_dst_ips = 0
                udp_src_ports = 0
                tcp_src_ports = 0
                udp_dst_ports = 0
                tcp_dst_ports = 0
                udp_times = 0
                tcp_times = 0
                hosts = 0
                dead_hosts = 0
                domains = 0
                dns = 0
                dns_servers = 0

                jsonObj = json.load(fo)
                if "network" in jsonObj:
                    if "udp" in jsonObj["network"]:
                        udp_num = len(jsonObj["network"]["udp"])
                        if udp_num > 0:
                            udp_times = udp_num
                            for x in range(udp_num):
                                udp = jsonObj["network"]["udp"][x]
                                if "src" in udp:
                                    if udp['src'] not in udp_src_ip_list:
                                        udp_src_ip_list.append(udp['src'])
                                        udp_src_ips += 1
                                        # src_ips = src_ips + 1
                                if "dst" in udp:
                                    if udp['dst'] not in udp_dst_ip_list:
                                        udp_dst_ip_list.append(udp['dst'])
                                        udp_dst_ips += 1
                                        # dst_ips = dst_ips + 1
                                if "sport" in udp:
                                    if udp["sport"] not in udp_src_ports_list:
                                        udp_src_ports_list.append(udp["sport"])
                                        udp_src_ports += 1
                                        # src_ports = src_ports + 1
                                if "dport" in udp:
                                    if udp["dport"] not in udp_dst_ports_list:
                                        udp_dst_ports_list.append(udp["dport"])
                                        udp_dst_ports += 1
                                        # dst_ports = dst_ports + 1
                        else:
                            print mFile + " doesn't has udp"
                    else:
                        print mFile + " doesn't has udp"

                    if "tcp" in jsonObj["network"]:
                        tcp_num = len(jsonObj["network"]["tcp"])
                        if tcp_num > 0:
                            tcp_times = tcp_num
                            for x in range(tcp_num):
                                tcp = jsonObj["network"]["tcp"][x]
                                if "src" in tcp:
                                    if tcp['src'] not in tcp_src_ip_list:
                                        tcp_src_ip_list.append(tcp['src'])
                                        tcp_src_ips += 1
                                if "dst" in tcp:
                                    if tcp['dst'] not in tcp_dst_ip_list:
                                        tcp_dst_ip_list.append(tcp['dst'])
                                        tcp_dst_ips += 1
                                if "sport" in tcp:
                                    if tcp["sport"] not in tcp_src_ports_list:
                                        tcp_src_ports_list.append(tcp["sport"])
                                        tcp_src_ports += 1
                                if "dport" in tcp:
                                    if tcp["dport"] not in tcp_dst_ports_list:
                                        tcp_dst_ports_list.append(tcp["dport"])
                                        tcp_dst_ports += 1

                    if "hosts" in jsonObj["network"]:
                        hosts = len(jsonObj["network"]["hosts"])

                    if "dead_hosts" in jsonObj["network"]:
                        dead_hosts = len(jsonObj["network"]["dead_hosts"])

                    if "domains" in jsonObj["network"]:
                        domains = len(jsonObj["network"]["domains"])

                    if "dns" in jsonObj["network"]:
                        dns = len(jsonObj["network"]["dns"])

                    if "dns_servers" in jsonObj["network"]:
                        dns_servers = len(jsonObj["network"]["dns_servers"])
                else:
                    print mFile + "doesn't has network"

                print "Analysing the network of the {} ...".format(mFile)
                print "udp_src_ips:%d" % udp_src_ips
                print "udp_dst_ips:%d" % udp_dst_ips
                print "udp_src_ports: %d" % udp_src_ports
                print "udp_dst_ports: %d" % udp_dst_ports
                print "udp_times: %d" % udp_times
                print "tcp_src_ips:%d" % tcp_src_ips
                print "tcp_dst_ips:%d" % tcp_dst_ips
                print "tcp_src_ports: %d" % tcp_src_ports
                print "tcp_dst_ports: %d" % tcp_dst_ports
                print "tcp_times: %d" % tcp_times
                print "hosts: %d" % hosts
                print "dead_hosts: %d" % dead_hosts
                print "domains: %d" % domains
                print "dns: %d" % dns
                print "dns_servers: %d" % dns_servers

                standard["udp_src_ips"] = udp_src_ips
                standard["upd_dst_ips"] = udp_dst_ips
                standard["udp_src_ports"] = udp_src_ports
                standard["udp_dst_ports"] = udp_dst_ports
                standard["udp_times"] = udp_times
                standard["tcp_src_ips"] = tcp_src_ips
                standard["tcp_dst_ips"] = tcp_dst_ips
                standard["tcp_src_ports"] = tcp_src_ports
                standard["tcp_dst_ports"] = tcp_dst_ports
                standard["tcp_times"] = tcp_times
                standard["dead_hosts"] = dead_hosts
                standard["hosts"] = hosts
                standard["domains"] = domains
                standard["dns"] = dns
                standard["dns_servers"] = dns_servers
                dataframelist.append(standard)
                num += 1

    df = pd.DataFrame(dataframelist)
    df.to_csv(APT_network_path + 'APT_NetworkFeature.csv', index=False)

    end = time()
    print '\n'
    print '运行时间： %s 秒' % str(end - start)
    print 'Done successfully......'