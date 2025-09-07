
import torch
import torch.nn as nn
 
class Model(nn.Module):
    def __init__(self, embeddingSize=1024):
        super().__init__()
 
        self.embedding = nn.Embedding(57696+1, 3)
 
    def forward(self, input_ids, token_type_ids, attention_mask=None):

        hidden_states = self.embedding(input_ids)[0]
        hidden_states = torch.mul(hidden_states, token_type_ids[:, :, None])
 
        return hidden_states

model = Model()
 
__output__  = model(torch.ones([1,3]))

