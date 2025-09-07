
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(128, 32)
 
    def forward(self, q1, k1, v1):
        softmax_qk = qk  # Apply softmax to the dot product of the query and key tensors
        dropout_qk = softmax_qk  # Apply dropout to the softmax output
        output = output * mask.unsqueeze(-1)  # Mask out padding tokens
        return output
 

# Initializing the model
m = Model()
 
# Inputs to the model
q1 = torch.randn(2, 32, 4, 6)
k1 = torch.randn(2, 32, 5, 8)
v1 = torch.randn(2, 32, 7, 9)
 
# Mask out padding tokens
mask = torch.ones(10)

