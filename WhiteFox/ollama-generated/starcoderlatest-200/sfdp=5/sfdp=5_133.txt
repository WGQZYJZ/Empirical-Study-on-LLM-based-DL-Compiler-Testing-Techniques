
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0., activation="relu",
                 num_layers=1):
        super().__init__()
        layers = []
        for _ in range(num_layers - 1):
            layers.append(nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward,
                                                   dropout=dropout, activation=activation))
        self.transformer = nn.TransformerEncoder(layers)
 
    def forward(self, x1, x2):
        x1 = self.transformer(x1, x2)
        return x1


# Initializing the model and loading the weights from a pre-trained model 
m = Model()
m.load_state_dict(torch.load("model.pt"))
# Inputs to the model
q = torch.randn(1, 3, 64, 64)
k = torch.randn(1, 3, 64, 64)
