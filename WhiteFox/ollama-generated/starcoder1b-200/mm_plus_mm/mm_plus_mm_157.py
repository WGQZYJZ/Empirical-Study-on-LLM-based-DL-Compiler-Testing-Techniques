
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Perform matrix multiplication with input1 and input2 to obtain a matrix containing the results of matrix multiplication between input1 and input2
        v2 = t3  + t4  # Add two results from matrix multiplication between input3 and input4 to get the result from the addition
        return v2


# Initializing the model
m = Model()


