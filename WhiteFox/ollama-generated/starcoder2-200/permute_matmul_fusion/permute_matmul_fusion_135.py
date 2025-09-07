
class Model(torch.nn.Module):
    def __init__(self, a = 0):
        super().__init__()
        self.a1  = torch.nn.Linear(2 , 3)

    def forward(self, x1):

        if (a == True):
            v1_a1 = self.a1.weight.permute(...) # Permute the weight of Linear layer a1
            v1   = torch.bmm(x1 , v1_a1)
        else:
            v2  = x1.permute(...).matmul(self.linear.weight, bias=None) # Apply bmm on permuted tensor and un-permuted weight.

        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1_a = torch.randn(10, 50)   # input A which will be permute first and then BMMed with permuted B
x1_b = torch.randn(2, 3, 4 ) # input B which will be permute first before being used in the BMM.
x1_c = torch.randn(50, 7 ,8) # input C which is permuted by itself at the beginning.

# In case of BMM, the inputs are: x1 and x2. And we don't care if x1 and x2 are permuted or not.
__output_a = m(x1, a=True)  # Passing 'A' in input_a
__output_b = m(x1, b=False)  # Passing 'B' in input_a
# In case of Matmul, the inputs are: x1 and x2. And we don't care if x1 and x2 are permuted or not.
__output_c = m(x1, a=True)  # Passing 'A' in input_b
__output_d = m(x1, b=False)  # Passing 'B' in input_b
