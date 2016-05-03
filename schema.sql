drop table if exists images;
create table images (
  id integer primary key autoincrement,
  filepath text not null,
  date date not null
);
