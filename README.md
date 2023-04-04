# APTMalInsight
# This project aims to detect and classify the APT malware based on dynamic features including the API, API category, File, Network, Registry information. When using the API information, we calculate the discriminative contributions 
# based on the CT-IDF algorithm. Furthermore, we generate the topology list from the api-api category pair list. We define some malicious behavioral patterns including malicious file operations, process operations, and network operations,
# because these operations usually indicate some degree of malicious contents.

The order of running the project is as follows:
1) Generate the Json files of the APT malware samples by executing these samples in the Sandbox
2) Run Get_Behavior_From_Json.py to extract the behavioral features from the generated Json files
     # get_all_APT_api(dir_path, curDir[:-5], mFile)
     # get_APT_api(dir_path, mFile)
     # get_category(filename)
     # get_pe_section(filename)
     # get_pe_imports(filename)
3) Run ApiStat.py to calculate the occurrences of API
     #api_of_all_classes()
	   #api_of_one_class()
	   #api_of_one_file()
	   #api_of_var_in_one_class()
4) Run Ctfidf.py to generate the discriminative contributions of every API based on the CT-IDF algorithm
5) Run APT_Api_Feature.py to generate the API feature based on their contributions
6) Run APT_apiCateFeature.py to generate the API category feature
7) Run APT_FileFeature.py to genereate the file operation feature
8) Run APT_NetworkFeature.py to generate the network operation feature
9) Run APT_RegistryFeature.py to generate the registry operation feature
10) Run APT_BiClassify.py to conduct binary detection between the malicious APT malware with the benigh programs
11) Run APT_MultiClassify.py to conduct multi-class detection among the APT malware samples
12) Run Generate_Ontopology_String_From_ApiList.py to generate the malicious ontopology list from the API-API category pair list
