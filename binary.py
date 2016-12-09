def bin8_rev(data): 
	data=((data & 0xF0)>>4) | ((data & 0x0F)<<4)
	data=((data & 0xCC)>>2) | ((data & 0x33)<<2)
	data=((data & 0xAA)>>1) | ((data & 0x55)<<1)
	return data; 


def bin16_rev(data): 

	data = ((data & 0xFF00) >> 8) | ((data & 0x00FF) << 8)
	data = ((data & 0xF0F0) >> 4) | ((data & 0x0F0F) << 4)
	data = ((data & 0xCCCC) >> 2) | ((data & 0x3333) << 2)
	data = ((data & 0xAAAA) >> 1) | ((data & 0x5555) << 1)

	return data

def bin32_rev(data): 

	data = ((data & 0xFFFF0000) >> 16) | ((data & 0x0000FFFF) << 16)
	data = ((data & 0xFF00FF00) >> 8) | ((data & 0x00FF00FF) << 8)
	data = ((data & 0xF0F0F0F0) >> 4) | ((data & 0x0F0F0F0F) << 4)
	data = ((data & 0xCCCCCCCC) >> 2) | ((data & 0x33333333) << 2)
	data = ((data & 0xAAAAAAAA) >> 1) | ((data & 0x55555555) << 1)

	return data

def bin64_rev(data): 

	data = ((data & 0xFFFFFFFF00000000) >> 32) | ((data & 0x00000000FFFFFFFF) << 32)
	data = ((data & 0xFFFF0000FFFF0000) >> 16) | ((data & 0x0000FFFF0000FFFF) << 16)
	data = ((data & 0xFF00FF00FF00FF00) >> 8) | ((data & 0x00FF00FF00FF00FF) << 8)
	data = ((data & 0xF0F0F0F0F0F0F0F0) >> 4) | ((data & 0x0F0F0F0F0F0F0F0F) << 4)
	data = ((data & 0xCCCCCCCCCCCCCCCC) >> 2) | ((data & 0x3333333333333333) << 2)
	data = ((data & 0xAAAAAAAAAAAAAAAA) >> 1) | ((data & 0x5555555555555555) << 1)

	return data
