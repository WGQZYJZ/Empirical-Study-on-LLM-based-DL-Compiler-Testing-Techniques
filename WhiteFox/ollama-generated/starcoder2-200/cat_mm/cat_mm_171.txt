
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1[0], x1[1]) # Matrix multiplication of two input tensors in the list x1
        v2 = torch.cat([v1] * len(x1), 1) # Concatenation of the result tensor along dimension 1, where the number of times the matrix multiplication result is concatenated depends on the length of the list
        return v2
# Initializing the model
m = Model()

