
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Matmul()

    def forward(self, query):
        key  = torch.rand(1024) 
        value = torch.rand(1024)
        scale_factor  = torch.rand(()) * 6 - 3 # Generate a random float number from [-3, 3]
        dropout_p  = torch.rand(())
        
        v1  = query @ key.t()
        v2  = v1 * scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = softmax_qk.dropout(p=dropout_q) 
        v5  = v4@value
        return v5

# Initializing the model
m  = Model()

# Inputs to the model
query = torch.rand(20, 32)

