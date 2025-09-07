
class AttentionModel(torch.nn.Module):
    def __init__(self, embeddim=768, nhead=12, dimk=None, dropout_p=0.1):
        super().__init__()

        if dimk is None:
            dimk = embeddim
        else:
            assert dimk % nhead == 0
            dimk = dimk // nhead
 
        self.embeddim = embeddim
        self.nhead = nhead
 
        attn_weight_layer = torch.nn.Linear(2 * embeddim, embeddim)

        self.query_layer1 = torch.nn.Linear(self.embeddim + dimk, 4*embeddim) # Embedding: dim+dimk -> 4*dim
        self.key_layer1 = torch.nn.Linear(self.embeddim + dimk, 4*embeddim)
 
        self.attn_weight_layer1 = attn_weight_layer 
        
        self.query_layer2 = torch.nn.Linear(4*embeddim + embeddim, nhead * embeddim) # Residual + Layer norm: 3*dim -> 4*dim
        self.key_layer2 = torch.nn.Linear(4*embeddim + dimk, nhead * embeddim)
 
        self.attn_weight_layer2 = attn_weight_layer
        self.output_layer1 = torch.nn.Linear(nhead * 4*embeddim, embeddim) # Layer norm: 4*dim -> 3*dim
        self.output_layer2 = torch.nn.Linear(embeddim + dimk , embeddim)
 
        self._reset_parameters()
 
    def _reset_parameters(self):
       for layer in [self.attn_weight_layer1,
                     self.attn_weight_layer2]:
           nn.init.xavier_uniform_(layer.weight)
   
        
   def forward(self, query, key):
        mask = torch.triu(torch.ones([query.size(-2), query.size(-3)], device=query.device)).bool()
 
        query1  = self.query_layer1(query + torch.dropout(key, p=.80, training=self.training))
        key1   = self.key_layer1(key)
        
        qk     = query1 @ key1.transpose(-2, -1) / math.sqrt(query1.size(-1))
        qk     = qk + mask
 

        attn_weight  = torch.softmax(qk, dim=-1) 
        attn_weight  = torch.dropout(attn_weight, p=.80, training=self.training) 
 
 
        vq  = self.attn_weight_layer2(query1 * attn_weight)
        vk  = self.attn_weight_layer2(key1 * attn_weight)
 
        vq = self.output_layer1(vq).transpose(-2, -3)
        vk = self.output_layer2(vk) # Residual and layer norm: 4*dim -> 4*dim
 
     
        output  = (vq + vk) * math.sqrt(.50)
        return vq


model1 = AttentionModel()

