
class Model(torch.nn.Module):
    def __init__(self, embedding_size=10, num_classes=2):
        super().__init__()
        self.embedding = torch.nn.Embedding(len(tokenizer), embedding_size)
        self.dropout  = torch.nn.Dropout(0.15)
        self.fc = torch.nn.Linear(embedding_size, num_classes)
 
    def forward(self, x1):
        v2 = self.embedding(x1).unsqueeze(dim=1)
        v3 = v2 * 0.5
        v4 = v3 + 1
        v5 = self.dropout(v4)
        return self.fc(v5).squeeze()


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 6, embedding_size=len(tokenizer), dtype=torch.float32)
