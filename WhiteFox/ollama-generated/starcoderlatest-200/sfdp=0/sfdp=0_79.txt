
class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.ff = torch.nn.Sequential(
            torch.nn.Linear(512 * 3, 1024),
            torch.nn.GELU(),
            torch.nn.Linear(1024, 768),
            torch.nn.Dropout(0.5)
        )
        self.dropout = torch.nn.Dropout(0.5)
 
    def forward(self, x):
        attention_output = ...

        output = self.ff(attention_output + x)

        return self.dropout(output)


# Initializing the model
m = TransformerModel()

# Inputs to the model
x = torch.randn(128, 512 * 3)
