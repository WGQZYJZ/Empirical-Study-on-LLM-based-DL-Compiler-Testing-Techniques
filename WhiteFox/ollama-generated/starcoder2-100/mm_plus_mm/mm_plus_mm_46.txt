
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        v1 = torch.mm(input1, torch.randn(32 * 64 * 64)) # Matrix multiplication with a random matrix of size 32*64*64
        v2 = torch.mm(torch.randn(8, 8), torch.randn(32, 64, 64)) # Matrix multiplication between two random matrices of sizes 8 * 8 and 32 * 64 * 64
        v3 = v1 + v2 # Addition of the results of the matrix multiplications
        return v3
# Initializing model
m = Model()

