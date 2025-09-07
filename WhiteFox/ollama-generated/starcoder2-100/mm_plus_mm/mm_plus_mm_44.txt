
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        return v1 + v2


# Initializing the model and providing its input tensors:
m  = Model()

input1 = torch.randn(10, 5) # A random matrix of shape (10, 5) representing the first tensor.
input2 = torch.randn(5, 8) # A random matrix of shape (5, 8) representing the second tensor.

input3 = torch.randn(7, 4) # A random matrix of shape (7, 4) representing the third tensor.
input4 = torch.randn(4, 12) # A random matrix of shape (4, 12) representing the fourth tensor. 

