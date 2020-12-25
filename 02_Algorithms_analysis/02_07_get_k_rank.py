def get_k_rank(num_list,k):
	num_list.sort()
	return num_list[k-1]


get_k_rank([5,3,7,8,9,0],5)