
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.dropout(x1, p=0.5, training=True) # Dropout only in the evaluation phase
        v2 = torch.rand_like(v1, ... # Generate a tensor with the same size as input_tensor filled with random numbers 
        return v1 + x1

# Input to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
