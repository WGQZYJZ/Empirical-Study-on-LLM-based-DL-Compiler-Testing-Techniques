
import torch
class Model(torch.nn.Module):
    def __init__(self, hparams):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(**hparams)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        v1  = torch.dropout(self._prepare_attention_mask(query), self.dropout) # Apply dropout to the input
        v2  = self.attn(v1)[0] + v1 # Compute the dot product of query and key plus the first component in attn_output, which is the attention mask (plus the original input query)
        return v2
 
def _prepare_attention_mask(query):
    device = torch.device("cuda" if self._use_cuda() else "cpu")
    attn_mask  = torch.zeros((1,1), device=device) # Initialize an empty tensor for the attention mask with size (batch_size x query_length x 1)
    return attn_mask
