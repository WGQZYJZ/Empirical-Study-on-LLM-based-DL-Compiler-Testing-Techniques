
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        attn  = torch.softmax((query @ key.transpose(-2, -1)) / math.sqrt(key.size(-1)), dim=-1)
        output  = attn @ value
        return output


# Initializing the model
m  = Model()


