
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.q = torch.nn.Linear(768, 4096)
        self.kv = torch.nn.Linear(d_model, d_model * 3)
        self.out = torch.nn.Linear(d_model, 256)
 
    def forward(self, x):
        x  = F.dropout(self.q(x), p=0.1, training=self.training)
        x *= math.sqrt(float(self.kv.weight.shape[0]))
        # Apply linear transformation to the scaled dot product result
        x += self.kv(x).unsqueeze(-2)
        output = F.relu(self.out(x))
        return output

