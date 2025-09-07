
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self._embedding  = torch.nn.Embedding(32, 10)
        self._encoder    = torch.nn.TransformerEncoderLayer(d_model=8, nhead=4, dim_feedforward=512, dropout=0.7970681401395435)

    def forward(self, src):
        return self._encoder(self._embedding(src)).transpose(-1,-2)

# Initializing the model
m  = MyModel()

 # Inputs to the model
 src = torch.randint(low=0, high=32, size=(16,8))
 
## Running the test
