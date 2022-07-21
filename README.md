# github-actions

## Aprendizado de utilização do [GitHub Actions](https://github.com/actions)

- Neste repositório tem-se a utilização de um script bem simples que envia uma mensagem, via telegram, a cada hora.  

- São necessários os seguintes passos:  

1) Criar um diretório **.github** seguido de **workflows** (.github/workflows/main.yml) e depois criar um arquivo **main.yml** este arquivo pode ter qualquer nome, porém deve ser respeitada suas referências. Pode ver seus detalhes [main.yml](.github/workflows/main.yml):  

2) Para fazer o agendamento através de horas, pode ser utilizado o seguinte site que ajuda a criar o padrão: [crontab.guru](https://crontab.guru/).  

3) Criar o [requirements.txt](requirements.txt) para que a aplicação rode com todos os pacotes python instalados.

4) Caso precise usar variáveis de ambiente, onde é necessário guardar senhas de apis, banco de dados, etc.. então siga o procedimento conforme a figura:  

![figura1](/figuras/figura1.png)

5) O tutorial em https://www.youtube.com/watch?v=PaGp7Vi5gfM é excelente e ajudou muito para começar a aprender sobre github actions.  

