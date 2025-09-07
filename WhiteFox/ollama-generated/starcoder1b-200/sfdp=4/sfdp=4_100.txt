
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.query_fc = nn.Linear(8, 32, bias=False)
        self.key_fc   = nn.Linear(32, 64, bias=False)
 
    def forward(self, x1, x2):
        query = torch.cat((x1, x2), dim=1).transpose(-1, -2).contiguous()
        # We use the same weights for both the query and key at each layer, because:
        # (1) For each layer we are using different attention coefficients;
        #     (i) If a single attention coefficient is used across all layers in this model, the model has more features.
        #     (ii) The model's prediction may not be exactly the same as what you predict when trained from scratch.
        key = self.query_fc(self.key_fc(query)).transpose(-1, -2)  # shape [batch x 64 x 32]
        attn_mask = torch.ones(1, query.size(0), dtype=torch.float).to(x1.device)  # shape [1 x batch x 64]
        attn_weight = torch.softmax(attn_mask @ key, dim=-1)  # shape [batch x 32]
        output = attn_weight @ value  # shape [batch x 8]
        return output


# Initializing the model
m = Model()
__input__   = __output__
