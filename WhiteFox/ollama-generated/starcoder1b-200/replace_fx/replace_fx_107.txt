
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(v1, training=training) # Fallback random behavior will not be executed
        return v2

__model_name__ = 'dropout'
if __model_name__ == 'dropout':
    m = Model()

    # Inputs to the model
    x1  = torch.randn(1, 2, 2)
    y1 = m(x1)
