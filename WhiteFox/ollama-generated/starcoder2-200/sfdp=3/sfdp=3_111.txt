
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.randn(1) 
        self.dropout = torch.nn.Dropout2d() # Dropout layer to apply dropout to the output of the softmax layer
    
    def forward(self, query, key, value):
            v3  = torch.matmul(query, key.transpose(-2,-1)) * self.scale # compute dot product of query and key tensors
            v4  = v3.softmax(dim=-1)
            v5  = self.dropout(v4) # apply dropout to the softmax output
            return v5 @ value


# Initializing the model
m  = Model()

# Inputs to the model
q_input = torch.randn(2, 3 ,64, 8)
k_input = torch.randn(2,3,10,6)
v_input = torch.randn(2, 3,5,6)

