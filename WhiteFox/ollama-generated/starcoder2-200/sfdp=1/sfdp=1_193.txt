
class Model(torch.nn.Module):
    def __init__(self, inv_scale_factor, dropout_p):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 4096)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        dot_prod = query @ key.transpose(-1,-2) / inv_scale_factor 
        outs = torch.softmax(dot_prod,-1) * 0.98
        return outs

# Initializing the model
model = Model()

 # Inputs to the model

query  = torch.randn(5,4,64,32)
key    = torch.randn(5,7,32,16)
value  = torch.randn(5,8,16,4096)
__output__  = model(query, key, value)

