
class Model(torch.nn.Module):
    def __init__(self, num_classes=4000):
        super().__init__()
        self.model = TransformerModel()
 
    def forward(self, x1):
        v1 = self.model.encoder.embedding(x1)  # Get embedding for the input tensor x1
        output = self.model.encoder.transformer(v1, 20)
        return output


# Initializing the model
m = Model()


