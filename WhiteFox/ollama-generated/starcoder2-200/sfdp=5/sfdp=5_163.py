
class Model(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8, dim_feedforward=2048):
        super().__init__()

        self.query = torch.nn.Linear(d_model, 4 * d_model)
        self.key = torch.nn.Linear(d_model, 3 * d_model)
        self.value = torch.nn.Linear(d_model, d_model)
        self.attn = torch.nn.MultiheadAttention(
            d_model=d_model, nhead=nhead, dropout=0.)
        self.dropout = torch.nn.Dropout(p=0.1)

        self.__init__()
 
    def forward(self):
        query  = self.query() # Initialize query with the output of `torch.nn.Linear`
        key   = self.key()(query) # Initialize key with the output of `torch.nn.Linear`
        value = self.value(key) # Initialize value with the output of `torch.nn.Linear`

        return self.__output__

# Initializing the model
m  = Model()

