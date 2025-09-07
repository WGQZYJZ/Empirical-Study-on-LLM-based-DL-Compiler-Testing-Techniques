
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(2048, 128)
        self.key = torch.nn.Linear(3072, 1024)
        self.value = torch.nn.Linear(1024, 2048)
        self.scale = torch.nn.Parameter(torch.zeros(3))
 
    def forward(self, x):
        # TODO: Write your model forward function here
        query_layer = self.query(x).view(x.shape[0], -1)
        key_layer = self.key(x).view(-1, 2048).expand(x.shape[0], 2048)
        value_layer = self.value(x).view(-1, 2048).expand(x.shape[0], 2048)
        scaled_dot_product = torch.matmul(query_layer, key_layer) / (self.scale * self.scale.unsqueeze(-1))
        attention_weights = F.softmax(scaled_dot_product, dim=-1).unsqueeze(dim=-2)
        output = attention_weights.matmul(value_layer)  # TODO: Write your model forward function here
        return output


# Initializing the model
m = Model()


