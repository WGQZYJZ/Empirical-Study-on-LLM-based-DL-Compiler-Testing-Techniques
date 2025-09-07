
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # Input query, key and value tensors
        self.query = torch.randn((256, 10))
        self.key   = torch.randn((256, 8394))
        self.value = torch.randn((256, 1780))
 
        # Parameters for scaling the dot product
        self.scale_factor  = 3e-3
         
        # Parameters of the dropout mechanism
        self.dropout_p     = 0.1
 
    def forward(self):
        v1  = torch.matmul(self.query, self.key.transpose(-2, -1)) / math.sqrt(float(v1.size(-1))) * self.scale_factor
        v2  = torch.nn.functional.softmax(v1) 
        v3  = torch.nn.functional.dropout(v2, p=self.dropout_p)
        v4  = v3.matmul(self.value)
        return v4


# Initializing the model
m  = AttentionModel()
 
# Generating a query tensor for the input
v1  = torch.randn((50, 8)) 
 
# Inputs to the model
v2  = m(v1)

