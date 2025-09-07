
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 4096)
        self.key = torch.nn.Linear(512, 4096)
        self.value = torch.nn.Linear(512, 4096)

    def forward(self, input_tensor):
        # Compute the dot product of the query and key tensors
        qk = self.query(input_tensor).transpose(-2, -1) / math.sqrt(input_tensor.size(-1))

        # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)

        # Compute the dot product of the attention weights and the value
        value = self.value(attn_weight).transpose(-2, -1)  # Compute the dot product of the weighted sum and the output of the key/query layers

        return value


# Initializing the model
m = Model()


