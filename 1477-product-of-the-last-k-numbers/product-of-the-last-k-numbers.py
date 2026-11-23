class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 to act as a neutral multiplier
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the list since any product including this 0 will be 0
            self.prefix_products = [1]
        else:
            # Multiply the new number with the last accumulated product
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k >= current length, a 0 was encountered within the last k elements
        if k >= len(self.prefix_products):
            return 0
        
        # Integer division gives the exact product of the last k elements
        return self.prefix_products[-1] // self.prefix_products[-1 - k]
