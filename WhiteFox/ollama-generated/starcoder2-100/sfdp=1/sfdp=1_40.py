
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(32, 4 * 10)
 
    def forward(self, qk): 
        x1 = self.qkv(qk) # Compute the dot product of a query and key tensor with the size [64]
        scale_factor = torch.tensor([5]) 
        v1  = x1 / scale_factor  # Scale the dot product by an inverse scale factor
        softmax_qk  = v1 .softmax(dim=-2)  # Apply softmax to the scaled dot product with the size [3,64]
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5) 
        output  = dropout_qk @ torch.tensor([[[[1],[1],[1]]]])  # Compute the dot product of a value tensor and a dropout output with the size [3,64]
        return output

# Initializing the model
m  = Model()

