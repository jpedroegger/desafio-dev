from django import template


register = template.Library()


@register.filter(name='preco')
def formata_preco(val):
    return f'R$ {val}'.replace('.', ',')
