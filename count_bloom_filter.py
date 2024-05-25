import hashlib
from bitarray import bitarray


class CountBloomFilter:
    def __init__(self, bit_size: int, hash_function_list: list):
        self.bit_size = bit_size
        self.bit_array = [0]*self.bit_size
        self.hash_function_list = hash_function_list

    def _get_hash_index(self, hash_func, data: str):
        return int(hash_func(data.encode()).hexdigest(), 16) % self.bit_size
    
    def add_data(self, data: str):
        for hash_func in self.hash_function_list:
            index = self._get_hash_index(hash_func, data)
            self.bit_array[index] += 1

    def check_data_existed(self, data: str):
        result = True
        for hash_func in self.hash_function_list:
            index = self._get_hash_index(hash_func, data)
            result &= (self.bit_array[index] > 0)
        
        return result
    
    def reset(self):
        self.bit_array = [0]*len(self.bit_array)

    def remove_data(self, data: str):
        for hash_func in self.hash_function_list:
            index = self._get_hash_index(hash_func, data)
            if self.bit_array[index] > 0:
                self.bit_array[index] -= 1


if __name__ == '__main__':
    bit_size = 1000
    hash_function_list = [hashlib.md5, hashlib.sha1, hashlib.sha256]
    cbf = CountBloomFilter(bit_size, hash_function_list)
    cbf.add_data("test")
    cbf.check_data_existed("test")
    cbf.remove_data("test")
    cbf.check_data_existed("test")