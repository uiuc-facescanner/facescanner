drop table if exists images;
create table images (
  id integer primary key autoincrement,
  filepath text not null,
  scanned boolean not null
);
