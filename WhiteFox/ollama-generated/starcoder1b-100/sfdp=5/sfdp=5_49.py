
class Model(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.embedding = torch.nn.Embedding(10000, d_model)
        self.encoder = Encoder(d_model, heads=8)

    def forward(self, input_ids, attention_mask, token_type_ids):
        embedding = self.embedding(input_ids)
        output = self.encoder(embedding, token_type_ids=token_type_ids)
        return output


# Initializing the model
m = Model(2048)


# Inputs to the model
input_ids = torch.zeros((1, 2), dtype=torch.int64).unsqueeze(0)
attention_mask = torch.zeros((1, 2), dtype=torch.float32).unsqueeze(0)
token_type_ids = torch.zeros((1, 2), dtype=torch.int64).unsqueeze(0)
