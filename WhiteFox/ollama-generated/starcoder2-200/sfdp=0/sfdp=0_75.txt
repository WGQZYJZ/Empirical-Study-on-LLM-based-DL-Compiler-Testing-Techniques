
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.embedding = torch.nn.EmbeddingBag(2017, 64)
 
    def forward(self, x1):

        batch_size  = len(x1[0])
        key_padding_mask  = [torch.zeros(batch_size).byte()]
        inv_scale  = 8
        
        query  = torch.randn((batch_size, 64)) 
        key    = torch.randn((2017, 64))
 
        v1  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        scaled_dot_product  = v1.softmax(dim=-1)
       
        attention_weights = scaled_dot_product.masked_fill_(key_padding_mask[0], -1e9).softmax(
            dim=-1
        )
 
        v5  = torch.rand((2017, 64))
        v6  = key[attention_weights].sum(dim=1)
        
        self._reset()
        self.embedding.weight[key[1][0]] 
        v8   = torch.arange(batch_size).to(torch.int32)[-self.num_embeddings:]
        v9, v10  = torch.meshgrid((v6, v5))

        v4    = self._pad_mask(self.weight)
        return v4
