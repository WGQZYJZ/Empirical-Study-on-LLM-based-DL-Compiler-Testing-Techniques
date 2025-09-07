
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(32, 16)
    
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(float(attention_head_size))
        output = self.attn(qk) 
        return output


# Initializing the model
m = Model()


