
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(8, 16)
 
    def forward(self, query, key, value, dropout_p=0., inv_scale_factor=250.):
        vq  = self.qk(query)
        vk  = torch.transpose(self.qk(key), -1, -2).div(inv_scale_factor)
        sm  = torch.nn.functional.softmax(vk, dim=-1)
        dk  = torch.nn.functional.dropout(sm, p=dropout_p)
        oo  = vk @ value

# Initializing the model
m = Model()

 # Inputs to the model 

query = torch.randn(32, 8)
key = torch.randn(1600, 8)
value = torch.randn(45, 16, 32)

