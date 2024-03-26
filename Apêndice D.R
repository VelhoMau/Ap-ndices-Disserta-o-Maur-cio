setwd("C:/Users/mauri/Desktop/Novos Testes/RRphylo")
library(ape)
library(RRphylo)
arvore <- read.tree("output_tree.tre")

fix.poly(arvore,type="resolve")->arvore.fixed

par(mfrow=c(1,2))
plot(arvore,no.margin=TRUE,show.tip.label=FALSE)
plot(arvore.fixed,no.margin=TRUE,show.tip.label=FALSE)

write.tree(arvore.fixed, file = "Arvore.newick")

ArvoreFixed <- read.tree("arvore.newick")
