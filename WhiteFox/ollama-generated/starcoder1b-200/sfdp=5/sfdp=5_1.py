
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 1024)
        self.key = torch.nn.Linear(256, 1024)
        self.value = torch.nn.Linear(1024, 1024)

    def forward(self, x1):
        attn_mask = (x1 == 0).unsqueeze(-1) # Add the attention mask to the input tensor

        query = F.dropout(self.query(x1), p=0.5, training=self.training, inplace=False) 
        key   = self.key(x1)
        
        value = F.dropout(self.value(x1), p=0.5, training=self.training, inplace=False) 
        attn_weight = torch.softmax(query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)), dim=-1)  # Compute the dot product of the query and key
        attn_weight = F.dropout(attn_weight, p=0.5, training=self.training, inplace=False) # Apply dropout to the softmax output

        return attn_weight @ value  # Compute the dot product of the dropout output and the value


# Initializing the model
m = Model()


