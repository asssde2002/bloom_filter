import hashlib
from bitarray import bitarray


class BloomFilter:
    def __init__(self, bit_size: int, hash_function_list: list):
        self.bit_size = bit_size
        self.bit_array = bitarray(self.bit_size)
        self.hash_function_list = hash_function_list

    def _get_hash_index(self, hash_func, data: str):
        return int(hash_func(data.encode()).hexdigest(), 16) % self.bit_size
    
    def add_data(self, data: str):
        for hash_func in self.hash_function_list:
            index = self._get_hash_index(hash_func, data)
            self.bit_array[index] = 1

    def check_data_existed(self, data: str):
        result = True
        for hash_func in self.hash_function_list:
            index = self._get_hash_index(hash_func, data)
            result &= self.bit_array[index]
        
        return result
    
    def reset(self):
        self.bit_array.setall(0)
    

if __name__ == '__main__':
    bit_size = 1000
    hash_function_list = [hashlib.md5, hashlib.sha1, hashlib.sha256]
    bf = BloomFilter(bit_size, hash_function_list)
    bf.add_data("test")
    bf.check_data_existed("test")
