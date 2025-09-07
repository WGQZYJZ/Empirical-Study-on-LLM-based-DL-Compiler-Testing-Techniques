
class Model(torch.nn.Module):
    def __init__(self, query=None, key=None, value=None):
        super().__init__()
 
        self._scale = torch.tensor([0.794251]) # scaling factor (a constant)
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

        self.att = nn.MultiheadAttention(embed_dim=self._scale, num_heads=4, dropout=.5)
        
        if query is not None and key is not None and value is not None:
            print(query, key, value)
            self.att = self.att(query, key, value)
        
    def forward(self):
        self.conv  = self.conv + nn.Dropout(.2)(self._scale)

        self.conv  = self.conv.relu()
        return self.conv

# Initializing the model
m = Model()

