%%
%% jicspack.cls Copyright (C) JICS
%%
%% This is the file: ``jicspack.cls",
%% 
%% This file may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.2
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%    http://www.latex-project.org/lppl.txt
%% and version 1.2 or later is part of all distributions of LaTeX
%% version 1999/12/01 or later.
%%
%% Documentclass inherited
%%    article
%%
%% Package required:    
%%    ifthen, fancyhdr, afterpage;
%% 
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\LoadClass[a4paper,12pt,twoside]{article}
\RequirePackage{ifthen}
\RequirePackage{fancyhdr}
\RequirePackage{afterpage}
\ProvidesClass{jicspack}
%add defn
\newtheorem{defn}{Definition}
\newtheorem{lem}{Lemma}
\newtheorem{pf*}{Proof}
\newtheorem{col}{Corollary}
\newtheorem{pro}{Proposition}

\newtheorem{thm}{Theorem}
%
\newboolean{isprint}
\newboolean{isissn}
\newboolean{isdate}
\setboolean{isdate}{false}
\setboolean{isissn}{false}
\setboolean{isprint}{false}
%
%new if
\DeclareOption{print}{%
\setboolean{isprint}{true}
}
\ProcessOptions
%end new if
\newbox\@issn
\def\setissn#1{
\setboolean{isissn}{true}
\setbox\@issn\hbox{\small #1 /}%//2011copyright
}
\newbox\@pubdate
\def\setpubdate#1{
\setboolean{isdate}{true}
\setbox\@pubdate\hbox{\small #1}
}
\def\@journal{Journal of Computational Information Systems}
\def\@journalheadsize{\small}
\def\@journalotherfont{\small\slant}
\def\volume{}
\def\year{}
\def\@pagerange{}
\def\@pagenumprefix{ }
\def\@no{1}
\def\setno#1{
\renewcommand{\@no}{#1}
}
\def\setvolume#1{
\renewcommand{\volume}{#1}
}
\def\setyear#1{
\renewcommand{\year}{#1}
}

\newcounter{firstpage}
\newcounter{temppage}

\setcounter{firstpage}{1}
\setcounter{temppage}{1}

\def\setpagerange#1#2{%
\renewcommand{\@pagerange}{\ #1--#2}
\setcounter{firstpage}{#1}
}

\ifthenelse{\boolean{isprint}}{%
\def\@thechangedpage{%
\@pagenumprefix\setcounter{temppage}{\value{firstpage}}
\addtocounter{temppage}{-1}
\addtocounter{temppage}{\value{page}}
\arabic{temppage}
}
}{}

%pagelayout definitions
\setlength{\textwidth}{495pt}
\setlength{\topmargin}{25pt}
\setlength{\oddsidemargin}{10pt}
\setlength{\evensidemargin}{-5pt}
\setlength{\marginparwidth}{5pt}
\setlength{\hoffset}{-25pt}
\addtolength{\voffset}{-30pt}

%\setlength{\footskip}{5pt}
\setlength{\headheight}{2pt}
\setlength{\textheight}{680pt}
\setlength{\headsep}{13pt}
\setlength{\parindent}{11pt}
\setlength{\parskip}{.85ex}


\def\@headauthor{}
\def\setheadauthor#1{%
\renewcommand{\@headauthor}{#1
}
}

  
\def\beginheader{
\ifthenelse{\boolean{isprint} \and {\value{page} > 1}}{

  \pagestyle{fancy}
  \fancyhf{}
  \fancyhead[RO,LE]{\@thechangedpage}
%%\fancyhead[C]{\small\textsl{\ \@headauthor\//\@journalheadsize\@journal\ \volume :\ \@no\ (\year)\ \@pagerange}}%这是原来的页眉居中的样子
  \fancyhead[RE,LO]{\small\textsl{\ \@headauthor\//\@journalheadsize\@journal\ \volume :\ \@no\ (\year)\ \@pagerange}}
  }
 {}
}
%end of definitions of pagelayout

%setup definitions
\def\justify@off{\let\\=\@normalcr
  \leftskip\z@ \@rightskip
  \@flushglue 
  \rightskip\@rightskip
  }
\def\justify@on{\let\\=\@normalcr
  \leftskip\z@ \@rightskip\z@ \rightskip\@rightskip}
\def\normal@text{\global\let\\=\@normalcr
  \global\leftskip\z@ \global\@rightskip\z@ \global\rightskip\@rightskip
  \global\parfillskip\@flushglue}
\def\fnstar#1{\@fnstar{\@nameuse{c@#1}}}
\def\@fnstar#1{\ifcase#1\or
    \hbox{$\star$}\or
    \hbox{$\star\star$}\or
    \hbox{$\star\star\star$}\or
    \hbox{$\star\star\star\star$}\or
    \hbox{$\star\star\star\star\star$}\or
    \hbox{$\star\star\star\star\star\star$}
  \else
    \@ctrerr
  \fi
  \relax}
\def\@belowfmskip{18\p@}
\def\xarabic#1{%
  \expandafter\expandafter\expandafter\ifnum\expandafter\the\@nameuse{c@#1}<0
  *\else\arabic{#1} \fi}
\newif\if@haskeywords             % If abstract / keywords: do not omit rules
\newbox\t@keyword                 % Box for keyword abstract
 \let\report@elt\@gobble

\def\runtitle#1{\gdef\@runtitle{#1}}
\def\runauthor#1{\gdef\@runauthor{#1}}
\let\@runauthor\relax
\let\@runtitle\relax
\let\@runningauthor\relax
\def\astsymbol#1{\@astsymbol{\@nameuse{c@#1}}}
\def\@astsymbol#1{\ifcase#1\or
    \hbox{$\ast$}\or
    \hbox{$\ast\ast$}\or
    \hbox{$\ast\ast\ast$}\or
    \hbox{$\ast\ast\ast\ast$}\or
    \hbox{$\ast\ast\ast\ast\ast$}\or
    \hbox{$\ast\ast\ast\ast\ast\ast$}%
  \else
    \@ctrerr
  \fi
  \relax}
\newif\if@JISCproofing
\@JISCproofingfalse

%end of definitions of setup

\AtBeginDocument{%
\ifthenelse{\boolean{isprint}}
{
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[L]{\small 
\ifthenelse{\boolean{isissn}}{\unhbox\@issn}{}
Copyright \copyright\ 2012 Binary Information Press\\
\ifthenelse{\boolean{isdate}}{\unhbox\@pubdate}{}
}
\renewcommand{\headrulewidth}{0pt}
%%%%%%
%\beginheader
%%%%%
}
{}
}

%define title
\newtoks\t@loc@notes              % List of notes for one element
\newcount\note@cnt                % Number of notes per element
\newcount\prev@elem \prev@elem=0  % Variables to keep track of
\newcount\cur@elem  \cur@elem=0   % types of elements that are processed

\def\@overtitleskip{69\p@}
\def\@undertitleskip{\z@}
\def\@titlesize{\Large\bfseries}
\chardef\e@title=1

\def\beg@elem{\global\t@loc@notes={}\global\note@cnt\z@}
\def\@xnamedef#1{\expandafter\xdef\csname #1\endcsname}
\def\add@xtok#1#2{\begingroup
  \no@harm
  \xdef\@act{\global\noexpand#1{\the#1#2}}\@act
\endgroup}
\def\no@harm{%
  \let\\=\relax  \let\rm\relax
  \let\ss=\relax \let\ae=\relax \let\oe=\relax
  \let\AE=\relax \let\OE=\relax
  \let\o=\relax  \let\O=\relax
  \let\i=\relax  \let\j=\relax
  \let\aa=\relax \let\AA=\relax
  \let\l=\relax  \let\L=\relax
  \let\d=\relax  \let\b=\relax \let\c=\relax
  \let\bar=\relax
  \def\protect{\noexpand\protect\noexpand}
}
\def\proc@elem#1#2{\begingroup
    \no@harm                             % make a few instructions harmless
    \let\thanksref\@gobble               % remove \thanksref from element
    \let\corauthref\@gobble
    \@xnamedef{@#1}{#2}%                 % and store as \@#1
    \let\thanksref\add@thanksref
    \let\corauthref\add@thanksref
    \setbox\@tempboxa\hbox{#2}%
  \endgroup
  \prev@elem=\cur@elem                   % keep track of type of previous
  \cur@elem=\csname e@#1\endcsname       % and current element
}


%(sub) define thanksref
\newtoks\t@glob@notes             % List of all notes
\def\note@sep{,}
\def\add@tok#1#2{\global#1\expandafter{\the#1#2}}
\def\add@thanksref#1{\global\advance\note@cnt\@ne
  \ifnum\note@cnt>\@ne \add@xtok\t@loc@notes{\note@sep}\fi
  \add@tok\t@loc@notes{\ref{#1}}}

\def\thanks{\@ifnextchar[{\@tempswatrue
  \thanks@optarg}{\@tempswafalse\thanks@optarg[]}}
\def\thanks@optarg[#1]#2{\refstepcounter{footnote}%
  \if@tempswa\label{#1}\else\relax\fi
  \add@tok\t@glob@notes{\footnotetext}%
  \add@xtok\t@glob@notes{[\the\c@footnote]}%
  \add@tok\t@glob@notes{{#2}}%
  \ignorespaces}

%(sub) end of definition of thanksref

\def\title#1{%
  \beg@elem
  \title@note@fmt                      % formatting instruction
  \add@tok\t@glob@notes                % for \thanks commands
    {\title@note@fmt}%
  \proc@elem{title}{#1}%
  \def\title@notes{\the\t@loc@notes}%  % store the notes of the title,
  \title@fmt{\@title}{\title@notes}%   % print the title
  \ignorespaces
}
\def\title@fmt#1#2{%
\@ifundefined{@runtitle}{\global\def\@runtitle{#1}}{}%
 \vspace*{12pt}             % Vertical space above title
  {\@titlesize #1\,\hbox{$^{#2}$}\par}%
  \vskip\@undertitleskip
\vskip24\p@  % Vertical space below title
}
\def\title@note@fmt{\def\thefootnote{\fnstar{footnote}}}
%end of definition of title
%%%%%define the received data%%
\newif\if@hasreceived
\newif\if@hasrevised
\newbox\@received
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\received#1{
\ifthenelse{\boolean{isprint}}{
\global\@hasreceivedtrue
\global\@hasrevisedfalse
\setbox\@received\hbox{\small Received\ #1}
}{}
}
\def\revised#1#2{
\ifthenelse{\boolean{isprint}}{
\global\@hasreceivedfalse
\global\@hasrevisedtrue
\setbox\@received\hbox{\small Received\ #1;\ revised \ #2}
}{}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%define ead and address
\newtoks\email@text
\newtoks\url@text
\def\email@name{Email address}
\def\emails@name{Email addresses}
\chardef\has@ead@email=0
\def\url@name{URL}
\def\urls@name{URLs}
\chardef\has@ead@url=0
\let\real@refstepcounter\refstepcounter

\newcommand\ead[1][email]{%
  \add@eadcomma{#1}%
  \expandafter\ifcase\csname has@ead@#1\endcsname
  \expandafter\global\expandafter\chardef
    \csname has@ead@#1\endcsname=1\relax\else
  \expandafter\global\expandafter\chardef
    \csname has@ead@#1\endcsname=2\relax\fi
  \add@ead{#1}%
}
\def\add@ead#1#2{%
  \expandafter\add@tok\csname #1@text\endcsname{\texttt{#2}\ead@au}%
  \expandafter\add@xtok\csname #1@text\endcsname{{\@author}}%
  \ignorespaces
}
\def\add@eadcomma#1{%
  \expandafter\ifcase\csname has@ead@#1\endcsname\else
  \expandafter\add@tok\csname #1@text\endcsname{, }\fi
}
\let\@ead@au\@empty
\def\ead@newau{\ifx\@ead@au\@empty\else\ead@addau\@ead@au
  \let\@ead@au\@empty\fi}
\let\ead@endau\ead@newau
\def\ead@addau#1{ (#1)}
\def\ead@au#1{\edef\@ead@au{#1}}

\def\@overaddressskip{2pt}
\def\@addressstyle{\small\itshape}
\newcounter{address}              % Address counter
\def\theHaddress{\arabic{address}}% for hyperref
\chardef\e@address=4
%\numberdef\e@address=4
%2011修改地址编号方式
%end of definition of ead
%begin define of address
\def\address{\@ifstar{\address@star}%
  {\@ifnextchar[{\address@optarg}{\address@noptarg}}}
\def\address@optarg[#1]#2{\real@refstepcounter{address}%
  \beg@elem
  \report@elt{address}\proc@elem{address}{#2}%
  \address@fmt{\c@address}{\the\t@loc@notes}{\@address}{#1}%
  \if@JISCproofing\else\label{#1}\fi
  \ignorespaces}
\def\address@noptarg#1{\real@refstepcounter{address}%
  \beg@elem
  \proc@elem{address}{#1}%
  \address@fmt{\z@}{\the\t@loc@notes}{\@address}{\theaddress}%
  \ignorespaces}
\def\address@star#1{%
  \beg@elem
  \proc@elem{address}{#1}%
  \address@fmt{\m@ne}{\the\t@loc@notes}{\@address}{*}%
  \ignorespaces}
\def\theaddress{\arabic{address}} %2011修改作者地址编号方式，由alph到arabic
\def\address@fmt#1#2#3#4{\@newelemtrue
  \if@JISCproofing\def\@eltag{#4}\else\def\@eltag{\theaddress}\fi
  \ifnum\prev@elem=\e@address \@newelemfalse \fi
  \if@newelem \address@fmt@init \fi
  \noindent \bgroup \@addressstyle
  \ifnum#1=\z@
    #3\,$^{\mathrm{#2}}$\space%
  \else
    \ifnum#1=\m@ne
      $^{\phantom{\mathrm{\@eltag}}}$\space #3\,$^{\mathrm{#2}}$%
    \else
      $^{\mathrm{\@eltag}}\space$#3\,$^{\mathrm{#2}}$%
    \fi
  \fi
  \par \egroup}
\def\address@fmt@init{%
  \par                                % Start new paragraph
   \vskip 6\p@ \@plus 3\p@ \@minus 1.5pt
   }
%end definition of address
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%define author

\chardef\e@author=2
\newtoks\corauth@text
\newcounter{corauth}
\def\author@font{}
\def\@authorsize{\large}
\newcounter{author}               % Author counter
\newcount\n@author                % Total number of authors
\def\n@author@{1}                 % idem, read from .aux file
\newif\if@firstauthor             % First author or collaboration?
\newif\if@newelem                 % Switch to new type of element?

\def\output@ead@text#1{%
  \expandafter\add@tok\csname #1@text\endcsname{\ead@endau}%
  \expandafter\ifcase\csname has@ead@#1\endcsname\else
  {\let\thefootnote\relax
    \footnotetext[0]{\raggedright\textit{%
        \expandafter\ifcase\csname has@ead@#1\endcsname\or
        \csname #1@name\endcsname\else
        \csname #1s@name\endcsname\fi
        : }%
        \expandafter\the\csname #1@text\endcsname.}}%
    \fi}
\def\runningauthor@fmt{%
  \begingroup\no@harm
    \if@firstauthor
      \ifnum0\n@author@ > 2
        \global\edef\@runningauthor{\@author\ et al.}%
      \else
        \global\let\@runningauthor\@author%
      \fi
    \else % \c@author > 1
      \ifnum0\n@author@ = 2
        \global\edef\@runningauthor{\@runningauthor\ \& \noexpand\@author}%
      \fi
    \fi
  \endgroup
}

\def\corauth{\@ifnextchar[{\@tempswatrue
  \corauth@optarg}{\@tempswafalse\corauth@optarg[]}}
\def\corauth@optarg[#1]#2{\refstepcounter{corauth}%
  \if@tempswa\label{#1}\else\relax\fi
  \add@tok\corauth@text{\footnotetext}%
  \add@xtok\corauth@text{[\the\c@corauth]}%
  \add@tok\corauth@text{{#2}}\ignorespaces}
\def\author{\@ifnextchar[{\author@optarg}{\author@optarg[]}}
\def\author@optarg[#1]#2{\stepcounter{author}%
  \beg@elem
  \add@tok\email@text{\ead@newau}%
  \add@tok\url@text{\ead@newau}%
  \@for\@tempa:=#1\do{\expandafter\add@thanksref\expandafter{\@tempa}}%
  \report@elt{author}\proc@elem{author}{#2}%
  %\ifnum0\n@collab@=\z@ \runningauthor@fmt \fi
  \author@fmt{\the\c@author}{\the\t@loc@notes}{\@author}%
}
\def\corauth@mark@fmt{\def\thecorauth{\hspace{-.05cm}\astsymbol{corauth}\hspace{-.05cm}}}
\def\output@corauth@text{\def\thefootnote{\astsymbol{footnote}}%
  \the\corauth@text}

\def\author@fmt#1#2#3{\@newelemtrue
  \if@firstauthor
  \first@author \global\@firstauthorfalse \fi
  \ifnum\prev@elem=\e@author \global\@newelemfalse \fi
  \if@newelem \author@fmt@init \fi
  \edef\@tempb{#2}\ifx\@tempb\@empty
    \hbox{{\author@font #3}}\else
    \hbox{{\author@font #3}\,$^{\mathrm{#2}}$}%
\fi}
\def\first@author{\author@note@fmt
  \corauth@mark@fmt
  \add@tok\t@glob@notes
  {\output@corauth@text
    \output@ead@text{email}%
    \output@ead@text{url}%
    \author@note@fmt}%
}%
\def\author@fmt@init{%
  \par
  \vskip 8\p@ \@plus 4\p@ \@minus 2\p@
  \@authorsize
  \leavevmode}                        % Vertical space above author list
 \def\and{\unskip~and~}
\def\author@note@fmt{\setcounter{footnote}{0}%
  \def\thefootnote{\xarabic{footnote}}
  }
\def\author@note@fmt{\setcounter{footnote}{0}%
  \def\thefootnote{\xarabic{footnote}}}
%end of definition of author
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%define abstract

\def\@preabstractskip{24\p@ \@plus 6\p@ \@minus 3\p@}
\def\@overabstractskip{8\p@}
\def\@preabstractskip{24\p@ \@plus 6\p@ \@minus 3\p@}
\def\@abstractwidth{.8\textwidth}
\def\@abstractsize{\fontsize{\@ixpt}{11pt}\selectfont}
\def\abstractname{Abstract}

\newbox\t@abstract                % Box for abstract
\newif\if@hasabstract             % If abstract / keywords: do not omit rules

\def\abstract{\@ifnextchar[{\@abstract}{\@abstract[]}}
\def\@abstract[#1]{%
  \global\@hasabstracttrue
  \global\setbox\t@abstract=\vbox\bgroup
  \leftskip\z@   
  \@rightskip\z@ \rightskip\@rightskip \parfillskip\@flushglue
   \small
  \parindent 1em                      % \parindent in abstract
  \noindent {\bfseries\centerline\abstractname}  % caption `Abstract' (bold)居中  
\vskip 0.5\baselineskip             % half a line of space below
\noindent\ignorespaces
}
\def\endabstract{\par \egroup}
%end of definition of abstract

%define keywords
\def\@overkeywordskip{12\p@}
\def\@keywordsize{\small}
\def\@keywordheading{{\textit{Keywords}:\ }}
\def\@keywordwidth{.8\textwidth}

\def\keyword{%
  \global\@haskeywordstrue             
  \def\sep{\unskip; }                  
  \global\setbox\t@keyword=\vbox\bgroup
  \@keywordsize
  \parskip\z@
  \vskip 10\p@ \@plus 2\p@ \@minus 2\p@  
  
  \justify@off                        
  \noindent\@keywordheading
  \ignorespaces
  }
\def\endkeyword{\par \egroup}
%end of definition of keywords

%define premaker
\def\premaker{%
\global\@hasabstractfalse       % Default:  no abstract or keywords
\global\@haskeywordsfalse       % Default:  no abstract or keywords
\global\@hasreceivedfalse       % Default:  no received or revised
\global\@hasrevisedfalse        % Default:  no received or revised
\let\@corresp@note\relax
\global\t@glob@notes={}\global\c@author\z@
\global\n@author=0\n@author@\relax
\global\c@address\z@
\global\advance\n@author\m@ne   % In comparisons later on we need
\global\@firstauthortrue        % set to false by first \author or \collab
\parskip 4\p@
\open@fm \ignorespaces
}
\def\endpremaker{%
   \ifx\@runauthor\relax
   \global\let\@runauthor\@runningauthor
  \fi
  \global\n@author=\c@author
  \if@hasreceived
  \unhbox\@received
  \fi
  \if@hasrevised
  \unhbox\@received
  \fi
  \if@hasabstract                       % IF abstract/ keywords THEN
   \vskip \@preabstractskip             % Space above rule
  %\hrule height 0.4\p@                  % Rule above abstract/keywords
    \vskip 8\p@
    \unvbox\t@abstract                  % print abstract, if any
  \fi
  \if@haskeywords                       % IF keywords THEN
    \vskip \@overkeywordskip
   {\unvbox\t@keyword}                  % Keyword abstract, if any
  \fi                                   % FI
  \vskip 10\p@
 % \hrule height 0.4\p@                  % rule below abstract/keywords%2011删除线  
  \vskip \@belowfmskip
  
   \close@fm                            % Close premaker.
   \output@glob@notes                   % Put notes at bottom of 1st page
  \let\address\relax
  \let\premaker\relax \let\endpremaker\relax
  \let\@maketitle\relax  \let\@@maketitle\relax
  \ifthenelse{\boolean{isprint}}
  {\protect\@journalprinthead}{}
}
%end of definition of premaker
\def\@journalprinthead{%
\thispagestyle{fancy}
%\fancyhf{}
\fancyhead[L]{\@journalheadsize\@journal\ \volume :\ \@no\ (\year)\ \@pagerange\ \\ Available at  http://www.Jofcis.com}
\pagestyle{empty}
}
%begin open & close fm
\newbox\fm@box                    % Box for collected premaker
\newdimen\fm@size                 % Total height of \fm@box
\newdimen\@premakerwidth
\@premakerwidth\textwidth

\let\maketitle\relax
\newdimen\t@xtheight
\t@xtheight\textheight \advance\t@xtheight-\splittopskip

\def\open@fm{\global\setbox\fm@box=\vbox\bgroup
  \hsize=\@premakerwidth                 
  \centering                                
  \hyphenpenalty\@M
}                                           
\def\close@fm{\egroup                       
  \fm@size=\dp\fm@box \advance\fm@size by \ht\fm@box
  \@whiledim\fm@size>\t@xtheight \do{%
    \global\setbox\@tempboxa=\vsplit\fm@box to \t@xtheight
    \unvbox\@tempboxa \newpage
    \fm@size=\dp\fm@box \advance\fm@size by \ht\fm@box}
    \unvbox\fm@box
}
\def\output@glob@notes{\bgroup
  \the\t@glob@notes
  \egroup}
%end of definition of open & close fm
\AtEndDocument{%
   \clearpage
   \addtocounter{page}{-1}%
   \addtocounter{page}{1}%
}
\newdimen\@bls                             
\@bls=\baselineskip                        
\def\small{\@setfontsize\small\@xipt{13.6}%
\abovedisplayskip 11\p@ \@plus3\p@ minus6\p@
\belowdisplayskip \abovedisplayskip
\abovedisplayshortskip  \z@ \@plus3\p@
\belowdisplayshortskip  5.5\p@ \@plus2.5\p@ minus3\p@
\def\@listi{%\leftmargin\leftmargini
 \parsep 0.1\p@ \@plus 1\p@ minus\p@ \itemsep \parsep
            \topsep 9\p@ \@plus3\p@ minus5\p@}}

\def\@bibliosize{\small}
\def\@biblabel#1{\hspace{-1cm}[#1]\hskip \z@ \@plus 1fill}
\def\thebibliography{%
  \@startsection{section}{1}{\z@}{20\p@ \@plus 8\p@ \@minus 4pt}
  {\@bls}{\Large\bfseries}*{\refname}%
\addcontentsline{toc}{section}{\refname}%
  \@thebibliography}
\let\endthebibliography=\endlist
\def\@thebibliography#1{
    %\flushleft
    \@bibliosize
  \list{\@biblabel{\arabic{enumiv}}}{\settowidth\labelwidth{\@biblabel{#1}}
    \itemsep 0.2\@bls \@plus 0.1\@bls \@minus 0.1\@bls
    \usecounter{enumiv}\let\p@enumiv\@empty
    \def\theenumiv{\arabic{enumiv}}}%
    \hbadness5000 \sfcode`\.=1000\relax}
    
    
\newenvironment{pf}%
  {\par\addvspace{\@bls \@plus 0.5\@bls \@minus 0.1\@bls}\noindent
   {\bfseries\proofname}\enspace\ignorespaces}%
  {\par\addvspace{\@bls \@plus 0.5\@bls \@minus 0.1\@bls}}
\def\proofname{PROOF.}
\@namedef{pf*}#1{\par\begingroup\def\proofname{#1}\pf\endgroup\ignorespaces}
\expandafter\let\csname endpf*\endcsname=\endpf

\def\descriptionlabel#1{\hspace\labelsep \bfseries #1}
\def\description{\list{}{\labelwidth\z@
  \leftmargin 1em \itemindent-\leftmargin
  \let\makelabel\descriptionlabel}}
\let\enddescription\endlist

\def\figurename{Fig.\small}
\def\tablename{Table \small}




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%此部分从原来模板的.tex中移来

\usepackage{enumerate}
\usepackage{graphicx}
\usepackage{amssymb}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%                     以下部分后加入                                       %%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{amsmath}%[tbtags]
\usepackage{amsfonts}
\usepackage{amsbsy}
\usepackage{latexsym,bm,amscd}
%\usepackage{amsthm}%此与\begin{defn}定义有冲突

%\usepackage{subfigure}
%\usepackage{wrapfig}%(P227)%图片类宏包
\usepackage{float}%(P225)不浮动的图形和表格

\usepackage{verbatim}
\usepackage{textcomp}%此宏包可以输入摄氏度符号\textcelsius
%\usepackage{multicol}

%\usepackage{tabularx}%自动计算列宽的宏包P108
\usepackage{dcolumn}%(P111)小数点对齐
\usepackage{booktabs}%表格类宏包
\usepackage{multirow}%表行合并
\newcolumntype{d}{D{.}{.}{-1}} %定义一个参数d,小数点后面可以含任意位数小数
\abovecaptionskip 3pt %标题到上文本之间的距离
\belowcaptionskip 3pt %标题到下文本之间的距离
\renewcommand{\arraystretch}{1.3}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newenvironment{mzk}[1]%
{\begin{list}{}{\renewcommand{\makelabel}[1]{\hspace*{3mm}\textrm{##1}\hfil}%
\settowidth{\labelwidth}{\textrm{#1}}%
\setlength{\labelsep}{3mm}%
\addtolength{\labelwidth}{\labelsep}%
\setlength{\parsep}{0.5mm}
\setlength{\itemsep}{0.5mm}%
\setlength{\leftmargin}{\labelwidth}}}%
{\end{list}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

