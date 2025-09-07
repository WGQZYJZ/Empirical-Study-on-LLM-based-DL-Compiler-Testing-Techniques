
class Model(torch.nn.Module):
    def __init__(self, attn_drop=0., res_layers=[6]):
        super().__init__()
 
        for i in res_layers:
            self.res_layers.append(torch.nn.Sequential(torch.nn.Linear(), torch.nn.Dropout()))

    def forward(self, query): 
        value = query
        for layer in self.res_layers:
            x  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
            x += attn_mask  # Add the attention mask to the scaled dot product
            attn_weight = torch.softmax(x, dim=-1) 
            attn_weight = torch.dropout(attn_weight, dropout_p=0., train=True)  
            output = attn_weight @ value 
        return v6


# Initializing the model
m  = Model()
 