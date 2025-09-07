import torch.nn as nn
from pytorch_pretrained_bert import BertModel
 
class Model(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.bert = BertModel(config)
 
    def forward(self, batch):
         _, cls_embed  = self.bert(batch['input'], return_dict=False)
         return cls_embed
