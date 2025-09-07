
import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0)  # Set dropout probability to 0%
        self.scale_factor = 1e-5
    
    def forward(self, query, key, value): 
        vq = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaledvq = vq / self.scale_factor  # Scale the dot product by the scale factor
        softmaxvqv = scaledvq.softmax(dim=-1)  # Apply softmax to the scaled dot product 
        droputqvqv = self.dropout(softmaxvqv)  # Apply dropout to the output of the softmax operation
        vqvqvw = torch.matmul(droputqvqv, value)  # Compute the dot product of the dropout output and a value tensor
        return vqvqvw

m  = Model()


# Initializing the model
x1 = torch.randn(256, 3072, requires_grad=True)
x2 = torch.randn(256, 3072, requires_grad=True)
x3 = torch.randn(256, 3072, requires_grad=True)
