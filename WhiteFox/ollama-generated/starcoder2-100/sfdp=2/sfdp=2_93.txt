
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
       scale = 1e-5
       
       v1 = torch.matmul(query, key.transpose(-2, -1)) / scale
       v3 = v1 + 0.7 * (torch.rand((v1.shape[0], 1) + v1.shape[-2:]) - 0.5).to(v1.device)
       
       v4 = torch.nn.functional.softmax(v3, dim=-1) 
       v5 = torch.nn.functional.dropout(v4, p=0.7 * dropout_p) 
       
       v6 = torch.matmul(v2, value).to(v2.device)
       
       return v6
 
m  = Attention()

 # Inputs to the model
q = torch.randn(batchsize, num_heads, qk_size, qv_size)
k = torch.randn(batchsize, num_heads, kv_size, qv_size)
v = torch.randn(batchsize, num_heads, qkv_size, v_size)

 # Initializing the model 
 __output__  = m(q, k, v)

# Model
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self._layers = nn.ModuleList([
            nn.Linear(in_features=4096 * 256, out_features=128), 
            nn.Dropout(), # dropout layer 
            nn.LeakyReLU()])
        self._output_layer = nn.Linear(in_features=128, out_features=7)

    def forward(self, x):
        return torch.softmax(self._output_layer(torch.cat([self._layers[0](x), self._layers[2](x)], dim=-1)),dim=-1)

 # Initializing the model
model  = MLP()
 
 # Inputs to the model 
 x  = torch.randn(64, 3958 * 7)
 
 # Generating the outputs of model for training purpose 
 