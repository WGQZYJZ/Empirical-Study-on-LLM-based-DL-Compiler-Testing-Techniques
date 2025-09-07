
class Model(torch.nn.Module):
    def __init__(self, scale=1024**-0.5, dropout=0.1):
        super().__init__()
        self.scale  = torch.full((3,), fill_value=scale)
 
        self.query  = torch.nn.Linear(786432, 3 * 3 * 8192)
        self.key   = torch.nn.Linear(786432, 3 * 3 * 512)
        self.value = torch.nn.Linear(786432, 3 * 3 * 2048)
 
    def forward(self, x):
        x = self.query(x).view(-1, 3*3*8192, 16384//8192)
        key   = self.key(x).view(-1, 3 * 3 * 512, 1024**-0.5)
        value = self.value(x).view(-1, 3*3*2048, 256//512)
 
        scaled_qk  = torch.nn.functional.layer_norm(key * self.scale, dim=-1) 
        softmax_qk = torch.nn.functional.softmax(scaled_qk + 32.)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
 
        return dropout_qk @ value

# Initializing the model