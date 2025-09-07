
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, qk, v):
        softmax_qk = self.softmax(qk) # Apply the softmax operation to the output of the dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk * v
        return output
 

# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(16, 8, 256, 10)
key    = torch.randn(16, 8, 256, 10)
scale_factor = torch.tensor(1/4).view(-1, 1, 1, 1) # Apply a factor of 1/4 to the dot product
