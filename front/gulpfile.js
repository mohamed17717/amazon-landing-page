const gulp = require('gulp');
const concat = require('gulp-concat');
const prefix = require('gulp-autoprefixer');
const sass = require('gulp-sass');
const livereload = require('gulp-livereload');
const sourcemaps = require('gulp-sourcemaps');

// CSS Task
gulp.task('scss', function(){
  return gulp.src(['stage/scss/*.scss'])
          .pipe(sourcemaps.init())
          .pipe(sass({outputStyle: 'compressed'}))
          .pipe(prefix('last 2 versions'))
          .pipe(concat('main.css'))
          .pipe(sourcemaps.write('.'))
          .pipe(gulp.dest('dist/css/'))
          .pipe(livereload());
});

// JS Task
gulp.task('js', function(){
  return gulp.src(['stage/js/*.js'])
          .pipe(sourcemaps.init())
          .pipe(concat('main.js'))
          .pipe(sourcemaps.write('.'))
          .pipe(gulp.dest('dist/js/'))
          .pipe(livereload());
});

// HTML task
gulp.task('html', function(){
  return gulp.src('stage/*.html')
          .pipe(gulp.dest('dist/'))
          .pipe(livereload());
});


// Watch Task
gulp.task('watch', function(){
  require('./server.js');
  livereload.listen();
  gulp.watch(['stage/*.html'], gulp.series('html'));
  gulp.watch(['stage/js/*.js'], gulp.series('js'));
  gulp.watch(['stage/scss/*.scss'], gulp.series('scss'));
});


gulp.task('default', gulp.series('watch'));